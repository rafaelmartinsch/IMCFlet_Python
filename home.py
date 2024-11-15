import flet as ft

def main(page:  ft.Page):
    page.title="Calculadora IMC"
    page.window.width=600
    page.window.alignment=ft.alignment.center
    
    def salvar(e):
        if altura_field.value!="" and peso_field.value!="":
            peso =  float(peso_field.value)
            altura_metros = float(altura_field.value)/100
            imc = peso/(altura_metros ** 2)
            
        if imc<18.5:
            resul_text.value=f"Seu IMC é {imc:.2f} - Abaixo do peso!"
            result_img.src="src/abaixo.png"
        elif imc<24.9:
            resul_text.value=f"Seu IMC é {imc:.2f} - Peso Normal!"
            result_img.src="src/normal.png"
        
        page.update()   
            
    
    def valida_altura(e):
        if not(altura_field.value.isnumeric() and int(altura_field.value)>0):
            altura_field.error_text="insira um valor númerico positivo"
            altura_field.value=None
        else:
            altura_field.error_text=None   
        page.update()
    
    def valida_peso(e):
        if not(peso_field.value.count(".") or peso_field.value.isdecimal() and int(peso_field.value)>0):
            peso_field.error_text="insira um valor númerico positivo"
            peso_field.value=None
        else:
            peso_field.error_text=None   
        page.update()
    
    page.appbar = ft.AppBar(
            title=ft.Text(
                          value="Cálculadora IMC", 
                          size=22, 
                          color="white", 
                          weight="bold"
                        ),
            center_title=True,
            bgcolor="#4CADE4"
            )
    
    altura_field = ft.TextField(
        label='Altura (cm)',
        width=300,
        hint_text="Por favor insira sua altura",
        on_change=valida_altura
    )
    
    peso_field = ft.TextField(
        label='Peso (kg)',
        width=300,
        hint_text="Por favor insira seu peso",
        on_change=valida_peso
    )
    
    resul_text =  ft.Text(
                    value="Insira as informações para começar!",
                    size=22,
                    width=150,
                    
                  )
    result_img =  ft.Image(src="src/imc.png", width=150, height="150")
    
    salvar_button = ft.ElevatedButton("Calcular", on_click=salvar)
    
    page.add(
        ft.Row(
            [
                ft.Column(
                    controls=[
                        ft.Row([resul_text,result_img], 
                               alignment=ft.MainAxisAlignment.CENTER 
                               ),
                        altura_field,
                        peso_field,
                        salvar_button
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ) 
            ],
            alignment=ft.MainAxisAlignment.CENTER,  
        )
    )
    
ft.app(main)