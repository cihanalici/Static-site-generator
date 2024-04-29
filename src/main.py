from textnode import TextNode
from htmlnode import LeafNode, ParentNode

def main():
    # node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(node)

    node2 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )

    node2.to_html()

main()
