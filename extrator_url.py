import re


class ExtractorURL:
    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.validate_url()

    def sanitize_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validate_url(self):
        if not self.url:
            raise ValueError("The URL is empty")

        url_pattern = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/convert")
        match = url_pattern.match(self.url)
        if not match:
            raise ValueError("Invalid URL")
        else:
            print("Valid URL")

    def search_parameter(self, parameter_search, parameter_end="&"):
        index_search = self.parameters.find(parameter_search)
        index_end = self.parameters.find(parameter_end, index_search)
        index_value = index_search + len(parameter_search)

        if index_end == -1:
            value = self.parameters[index_value + 1 :]
        else:
            value = self.parameters[index_value + 1 : index_end]
        return value

    def index_host(self):
        index_host = self.url.find("b")
        return index_host

    def index_path(self):
        index_path = self.url.find("/", self.index_host())
        return index_path

    def index_parameters(self):
        index_parameters = self.url.find("?", self.index_path())
        return index_parameters

    @property
    def protocol(self):
        protocol = self.url[: self.url.find(":")]
        return protocol

    @property
    def host(self):
        host = self.url[self.index_host() : self.index_path()]
        return host

    @property
    def path(self):
        path = self.url[self.index_path() : self.index_parameters()]
        return path

    @property
    def parameters(self):
        parameters = self.url[self.index_parameters() + 1 :]
        return parameters

    def __str__(self):
        return f"URL: {self.url} \nProtocol: {self.protocol} \nHost: {self.host} \nPath: {self.path} \nParameters: {self.parameters}\n"

    def __len__(self):
        return len(self.url)

    def __eq__(self, other):
        return self.url == other.url


url = ExtractorURL(
    "https://bytebank.com/convert?originalCurrency=real&convertedCurrency=dollar&amount=100"
)

print(url)
original_currency = url.search_parameter("originalCurrency")
converted_currency = url.search_parameter("convertedCurrency")
amount = url.search_parameter("amount")

dollarQuotation = 4.7

if original_currency == "real" and converted_currency == "dollar":
    value = float(amount) / dollarQuotation
    print(value)
elif original_currency == "dollar" and converted_currency == "real":
    value = float(amount) * dollarQuotation
    print(value)
else:
    raise Exception("Invalid currency")
