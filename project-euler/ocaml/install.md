# ocaml
sudo apt install opam
opam init -y
eval $(opam env)

## optional:
opam install dune ocaml-lsp-server odoc ocamlformat utop

## usage:

### iterpreter:
ocaml p1.ml

### compiled:
ocamlbuild p1.native