def buscar_parametro(parametros, parametro_busca, parametro_fim="&"):
    indice_busca = parametros.find(parametro_busca)
    indice_fim = parametros.find(parametro_fim, indice_busca)
    indice_valor = indice_busca + len(parametro_busca)

    if indice_fim == -1:
        valor = parametros[indice_valor + 1 :]
    else:
        valor = parametros[indice_valor + 1 : indice_fim]
    return valor


def sanitizaURL(url):
    return url.strip()


def verificaLinkVazio(url):
    if url == "":
        raise ValueError("A URL que você inseriu está vazia")


def main():
    url = (
        "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
    )

    url = sanitizaURL(url)
    verificaLinkVazio(url)

    indice_host = url.find("b")
    indice_parametros = url.find("?")
    protocolo = url[:indice_host]
    host = url[indice_host:indice_parametros]
    parametros = url[indice_parametros + 1 :]

    print(f"URL: {url}")
    print(f"Protocolo: {protocolo}")
    print(f"Host: {host}")
    print(f"Parâmetros: {parametros}")

    moeda_origem = buscar_parametro(parametros, "moedaOrigem")
    print(f"Moeda de Origem: {moeda_origem}")
    moeda_destino = buscar_parametro(parametros, "moedaDestino")
    print(f"Moeda de Destino: {moeda_destino}")
    quantidade = buscar_parametro(parametros, "quantidade")
    print(f"Quantidade: {quantidade}")


if __name__ == "__main__":
    main()
