import MesonAST

public class TypeAnalyzersState {
  let state: [String: MesonTypeAnalyzer]
  public init() {
    self.state = [
      "import": ImportTypeAnalyzer(), "get_option": OptionTypeAnalyzer(),
      "dict.get": DictGetTypeAnalyzer(), "list.get": ListGetTypeAnalyzer(),
    ]
  }
  public func apply(node: Node, options: [MesonOption], f: Function, ns: TypeNamespace) -> [Type] {
    if let c = self.state[f.id()] { return c.derive(node: node, fn: f, options: options, ns: ns) }
    return f.returnTypes
  }
}
