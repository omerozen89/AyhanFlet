from flet import *

def main(page:Page):
    page.title = "Ayhan Paryzada"
    page.scroll = 'auto'
    page.window.top = 1
    page.window.left = 960
    page.window.width = 390
    page.window.height = 740
    page.bgcolor = 'white'
    page.theme_mode = ThemeMode.LIGHT
    
    flashlight = Flashlight()
    page.overlay.append(flashlight)
    
    ph = PermissionHandler()
    page.overlay.append(ph)
    
    def open_app(e):
        ph.open_app_settings()
    

    page.add(
        
        AppBar(
            title = Text('Flash Light [AY]'),
            color='white',
            bgcolor='#e3113e',
            actions=[
                IconButton(icons.SETTINGS,on_click=open_app)
            ]
        ),
        
        Row([
            Text('\n\nFlash Light App',size=31,color='black')
        ],alignment=MainAxisAlignment.CENTER),
        
        Row([
           Image(src="logo.png",width=360) 
        ],alignment=MainAxisAlignment.CENTER),
        
        Row([
            ElevatedButton(
                "ON",
                width=100,
                icon=icons.PLAY_ARROW,
                style=ButtonStyle(
                    bgcolor="#e3113e",
                    color='white',
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda _: flashlight.turn_on()
            )
            ,
             ElevatedButton(
                "OFF",
                width=100,
                icon=icons.PLAY_DISABLED_SHARP,
                style=ButtonStyle(
                    bgcolor="#e3113e",
                    color='white',
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda _: flashlight.turn_off()
            )
            
            
        ],alignment=MainAxisAlignment.CENTER),
        
        Row([
            Text('\n\nAyhan App 2025',size=14,color='black')
        ],alignment=MainAxisAlignment.CENTER),
        
        
        
            
            
    )    

    page.update()
app(main)
