public class Subproject: AbstractObject {
  public let name: String = "subproject"
  public var methods: [Method] = []
  public let parent: AbstractObject? = nil

  public init() {
    self.methods = [
      Method(
        name: "found", parent: self,
        returnTypes: [
          BoolType()
        ]),
      Method(
        name: "get_variable", parent: self,
        returnTypes: [
          `Any`()
        ]),
    ]
  }
}
