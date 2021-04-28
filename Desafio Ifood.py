print("Ranking dos restaurantes: Próximos ao endereço de entrega, realizado por critérios de avaliação e valor do frete:" )
print()

kibon_Sorveteria_Saude = [4.9, 6.99, "Kibon Sorveteria - Saúde" ]
Makis_Place_Saude = [4.7, 7.99, "Makis Place - Saúde"]
Sukiya_Saude = [4.6, 7.99, "Sukiya - Saúde"]
Giraffas_Carrefour_Metrocar = [4.4, 5.99, "Giraffas Carrefour Metrocar"]
A_feijoada = [4.4, 9.90, "A feijoada"]
Viena_Shopping_Santa_Cruz = [4.4, 12.49, "Viena Shopping Santa Cruz" ]

lista_restaurantes = [kibon_Sorveteria_Saude, Makis_Place_Saude, Sukiya_Saude, Giraffas_Carrefour_Metrocar, A_feijoada, Viena_Shopping_Santa_Cruz]

for x in lista_restaurantes:
    if x == kibon_Sorveteria_Saude:
        print("1º: {} (nota {} com frete de R$ {})".format(x[2], x[0], x[1]))
    elif x == Makis_Place_Saude:
        print("2º: {} (nota {} com frete de R$ {})".format(x[2], x[0], x[1]))
    elif x == Sukiya_Saude:
        print("3º: {} (nota {} com frete de R$ {})".format(x[2], x[0], x[1]))
    elif x == Giraffas_Carrefour_Metrocar:
      print("4º: {} (nota {} com frete de R$ {})".format(x[2], x[0], x[1]))
    elif x == A_feijoada :
     print("5º: {} (nota {} com frete de R$ {})".format(x[2], x[0], x[1]))
    elif x == Viena_Shopping_Santa_Cruz :
     print("6º: {} (nota {} com frete de R$ {})".format(x[2], x[0], x[1]))