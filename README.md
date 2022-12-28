# Project Thema

Als project heb ik ervoor gekozen om een order api te maken.  Hierbij kan ik verschillende bestellingen maken waarbij ik een orderid krijg, 
dit orderid kan de klant dan gebruiken om informatie van zijn order te bekijken. Ook is het mogelijk om alle bestellingen te bekijken met een filters zoals enkel van bestellingen van een bepaald persoon.
Hiervoor heb ik gebruik gemaakt van 1 post 2 get. 

> POST "/register" Hiermee kan je een account aanmaken die je later kunt gebruiken om de token op te vragen.<br>
> GET "/customers" Dit geeft een lijst van alle klanten accounts.<br>
> GET "/customer/{user_id}" Hiermee kan je van een bepaalde user (via de userid) gegevens opvragen, zoals email, bestellingen, naam, etc.<br>
> POST "/customers/{customer_id}/orders" Hiermee kan ik een order aanmaken op de naam van een bepaalde klant via id en het product kiezen.<br>
> GET "/orders" Dit laat alle orders zien die er gemaakt zijn.
> PUT "/orders/{order_id}" Hiermee kan ik een bepaalde order aanpassen als je de orderid meegeeft.<br>
> DELETE "/orders/{order_id}" Hiermee kan je een order deleten aan de hand van een ordernummer.
> GET "/products" Dit laat alle mogelijke producten zien.
> POST "/products" Hiermee kan je een nieuw product aanmaken.
> POST "/token" Hiermee kan je een token opvragen via bepaalde inloggegevens, deze token kan je gebruiken om bepaalde requests te doen.
> GET "/users/me" Dit laat alle data zien van de gebruiken die is ingelogd via de token.

## Links
* API Links
    * [API Repository](https://github.com/ArneVangheel/API-Eindproject)
    * [Hosted API](https://api-eindproject-arnevangheel.cloud.okteto.net/)
* Front-End Links
    * [Front-End Repository](https://github.com/ArneVangheel/website-eindproject)
    * [Hosted Front-End ](https://api-eindproject.netlify.app/)
## Postman (API Testing)
> GET "/orders/{id}" laat informatie over 1 bepaald order zien aan de hand van een orderid.

![image](https://user-images.githubusercontent.com/94957070/202862989-4309ebd3-2e57-41c3-b21f-03c5a8c855a1.png)

> GET "/all_orders" geeft all orders weer.

![image](https://user-images.githubusercontent.com/94957070/202863091-29287ac0-482a-4465-acdd-b231a425a4d3.png)

> POST "/order" maak een bestelling aan.
![image](https://user-images.githubusercontent.com/94957070/202863134-1f799119-51b4-4920-9c2d-9b79d1dae142.png)

## OpenAPI Docs Screenshots
![image](https://user-images.githubusercontent.com/94957070/202858157-0b42e118-56f2-4f90-93ec-5c0f0ab79467.png)
![image](https://user-images.githubusercontent.com/94957070/202858168-447aa8ab-eb05-47f0-86ca-fcdeb8427588.png)
![image](https://user-images.githubusercontent.com/94957070/202858180-eac7f35e-bb31-457a-947d-d8c9b5403f0d.png)

## Website
Ook is het mogelijk om op de website gebruik te maken van een user filter.
![image](https://user-images.githubusercontent.com/94957070/202862896-f7fc8010-07e1-412c-bd4e-2cc3e63d8045.png)
Hierbij kunnen we orders gaan filter op voornaam.
![image](https://user-images.githubusercontent.com/94957070/202862938-d7f803b4-c9f0-47c1-a46f-be0aa9b8b31e.png)

Op deze pagina kan je een bestelling maken, als je deze indient krijg je een orderid die je kan gebruiken om informatie te vinden over je order.
![image](https://user-images.githubusercontent.com/94957070/202896662-51318522-6741-4e66-b36f-6f422cf0369f.png)

Hier krijg je meer informatie over je bestelling.
![image](https://user-images.githubusercontent.com/94957070/202896676-67ff6f1a-8748-439b-8dc0-4a7594e32fbe.png)

