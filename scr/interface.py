import easygui

def conversorTemperatura(valor):
    try:
        valorInteiro = float(valor)
        celsius = (valorInteiro - 32) * 5/9
        easygui.msgbox(f"O valor em CELSIUS: {celsius}", title="Resultado em Celsius")
    except ValueError:
        easygui.msgbox("Por favor, digite um numero valido")


valoEmFahrenheit = easygui.enterbox("Digite o valor em Fahrenheit:", title="Conversor de Fahrenheit em Celsius")
conversorTemperatura(valoEmFahrenheit)