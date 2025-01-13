tza_agua= int(input("cuantas tazas de agua son")) 
tza_Hpan= int(input("cuantas tazas de harina pan son"))
cda_aceite= int(input("cuantas cucharadas de aceite son"))
cdta_sal= int(input("cuantas cucharaditas de sal son"))
tazas_totales1=(tza_agua+tza_Hpan+cda_aceite/16+cdta_sal/48)
evaporacion= tazas_totales1/10
tazas_totales=tazas_totales1-evaporacion
print("La cantidad de tazas totales de la mezcla son",tazas_totales)