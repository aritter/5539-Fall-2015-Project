import cc.factorie.protobuf.DocumentProtos.Relation
import cc.factorie.protobuf.DocumentProtos.Relation.RelationMentionRef

import java.util.zip.GZIPInputStream
import scala.io._
import java.io._

import scala.collection.mutable.HashMap

class Guid2Name(mapFile:String, lower:Boolean) {
  def this(mapFile:String) = this(mapFile, false)

  val m2n = new HashMap[String,List[String]]
  val n2m = new HashMap[String,List[String]]

  for(line <- scala.io.Source.fromFile(mapFile).getLines()) {
    var Array(mid, rel, lang, name) = line.trim.split("\t")

    if(lower) {
      name = name.toLowerCase
    }

    if(!m2n.contains(mid)) {
      m2n += mid -> List()
    }
    m2n(mid) ::= name

    if(!n2m.contains(name)) {
      n2m += name -> List()
    }
    n2m(name) ::= mid
  }

  def apply(str:String):List[String] = {
    var s = guid2mid(str)
    if(lower) {
      s = str.toLowerCase
    }

    if(s(0) == '/') {
      if(!m2n.contains(s)) {
	return List[String]()
      } else {
	return m2n(s)
      }
    } else {
      if(!n2m.contains(s)) {
	return List[String]()
      } else {
	return n2m(s)
      }
    }
  }

  def guid2mid(guid:String) : String = {
    var GUID = guid
    //From Freebase wiki:
    /*
     * 1. Take the GUID
     * 2. Strip off the leading "#9202a8c04000641f8"
     * 3. Take what's left and interpret it as a hex number
     * 4. Express that number in base 32 using the character set 0123456789bcdfghjklmnpqrstvwxyz_ (ie the digits, the letters excluding the vowels and underscore)
     * Prepend /m/0 to what you've got.
     */
    val characters =List('0','1','2','3','4','5','6','7','8','9','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','_').toArray

    GUID = GUID.replace("/guid/", "")

    var result = List[Char]()
    var number = Integer.parseInt(GUID.slice(17,GUID.length), 16)
    //println(GUID)
    //println(GUID.slice(17,GUID.length))
    while(number > 0) {
      result ::= characters(number & 31)
      number >>= 5
    }
    
    return "/m/0" + result.mkString("")
  }
}

object ParseNYT {
  def main(args: Array[String]) {
    var is = new GZIPInputStream(new BufferedInputStream(new FileInputStream(args(0))))
    var r = Relation.parseDelimitedFrom(is);

    val g2n = new Guid2Name("mid2name")

    while(r != null) {
      val e1 = g2n(r.getSourceGuid)
      val e2 = g2n(r.getDestGuid)
      var relStrings = r.getRelType

      for(i <- 0 until r.getMentionCount) {
        val m = r.getMention(i)
        val sentence = m.getSentence
        for(j <- 0 until m.getFeatureCount) {
          var feature = m.getFeature(j)
          println((e1, e2, relStrings, sentence, feature))
        }
      }
      r = Relation.parseDelimitedFrom(is)
    }
  }
}
