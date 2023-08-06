import easygui

def conversorTemperaturaCelsius(valor):
    try:
        valorInteiro = float(valor)
        celsius = (valorInteiro - 32) * 5/9
        easygui.msgbox(f"O valor em CELSIUS: {celsius}", title="Resultado em Celsius")
    except ValueError:
        easygui.msgbox("Por favor, digite um numero valido")


def conversorTemperaturaFahrenheit(valor):
    try:
        valorInteiro = float(valor)
        fahrenheit = (valorInteiro * 9/5) + 32
        easygui.msgbox(f"O valor em fahrenheit: {fahrenheit}", title="Resultado em fahrenheit")
    except ValueError:
        easygui.msgbox("Por favor, digite um numero valido")


escolha = easygui.buttonbox("Escolha qual temperatura deseja converter." , choices=["Para Fahrenheit", "para Celsius"])

if escolha == "para Celsius":
    valoEmFahrenheit = easygui.enterbox("Digite o valor em Fahrenheit:", title="Conversor de Fahrenheit em Celsius")
    conversorTemperaturaCelsius(valoEmFahrenheit)
else:
    valorEmCelsius = easygui.enterbox("Digite o valor em Celcius:", title="Conversor para Fahrenheit")
    conversorTemperaturaFahrenheit(valorEmCelsius)
