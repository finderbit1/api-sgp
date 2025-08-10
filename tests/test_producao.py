from json import load,dump 
from pedidos.schema import FichaPedido

payload = """
acabamento: {overloque: true, elastico: true, ilhos: false}

altura: ""

descricao: "painel batmabn"

designer: "carol"

emenda: "sem-emenda"

ilhosDistancia: ""

ilhosQtd: ""

ilhosValorUnitario: ""

imagem: "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABtbnRyUkdCIFhZWiAH4AABAAEAAAAAAABhY3NwAAAAAAAAAAAAA…"

largura: ""

observacao: ""

tecido: ""

tipoProducao: "painel"

valorPainel: ""

valorpainel: "90,00"

vendedor: "carol"

Object Prototype"""



pedido = FichaPedido(**dump(payload))
print(pedido)
