print("Ranking dos restaurantes: Próximos ao endereço de entrega, realizado por critérios de avaliação e valor do frete:" )
print()

kibon_Sorveteria_Saúde = [4.9, 6.99, "Kibon Sorveteria - Saúde" ]
Makis_Place_Saúde = [4.7, 7.99, "Makis Place - Saúde"]
Sukiya_Saúde = [4.6, 7.99, "Sukiya - Saúde"]
Giraffas_Carrefour_Metrocar = [4.4, 5.99, "Giraffas Carrefour Metrocar"]
A_feijoada = [4.4, 9.90, "A feijoada"]
Viena_Shopping_Santa_Cruz = [4.4, 12.49, "Viena Shopping Santa Cruz" ]

lista_restaurantes = [kibon_Sorveteria_Saúde, Makis_Place_Saúde, Sukiya_Saúde, Giraffas_Carrefour_Metrocar, A_feijoada, Viena_Shopping_Santa_Cruz]

for x in lista_restaurantes:
    if x[0] >=4.9:
        print("1º: {} (nota {} com frete de R$ {})".format(x[2], x[0], x[1]))
    elif x[0] >= 4.7:
        print("2º: {} (nota {} com frete de R$ {})".format(x[2], x[0], x[1]))
    elif x[0] >= 4.4 and x[1] < 9.90:
        print("3º: {} (nota {} com frete de R$ {})".format(x[2], x[0], x[1]))
    elif x[0] >= 4.4 and x[1] <12.49:
        print("4º: {} (nota {} com frete de R$ {})".format(x[2], x[0], x[1]))
    else:
        print("5º: {} (nota {} com frete de R$ {})".format(x[2], x[0], x[1]))
