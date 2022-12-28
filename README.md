# Project Thema

Als project heb ik ervoor gekozen om een order api te maken. Dit is allemaal met een database verbonden, een table die de klanten accounts bewaard, een table voor de verschillende bestellingen, en dan een table die alle producten bewaard. Hierbij kan ik verschillende bestellingen voor bepaalde klanten aanmaken. Dit product kan ik kiezen uit de table, of ik kan ook nieuwe producten aanmaken. Ook heb ik het gemaakt, dat vooraleer je al deze dingen kunt doen moet inloggen/registreren op een website. Ook kan ik dan alle geregistreerde accounts bekijken, of data opvragen van een bepaalde klant. Ook kan ik een order aanpassen (dus bv de status naar Done zetten ipv Processing), en verwijderen.

> POST "/register" Hiermee kan je een account aanmaken die je later kunt gebruiken om de token op te vragen.<br>
> GET "/customers" Dit geeft een lijst van alle klanten accounts.<br>
> GET "/customer/{user_id}" Hiermee kan je van een bepaalde user (via de userid) gegevens opvragen, zoals email, bestellingen, naam, etc.<br>
> POST "/customers/{customer_id}/orders" Hiermee kan ik een order aanmaken op de naam van een bepaalde klant via id en het product kiezen.<br>
> GET "/orders" Dit laat alle orders zien die er gemaakt zijn.<br>
> PUT "/orders/{order_id}" Hiermee kan ik een bepaalde order aanpassen als je de orderid meegeeft.<br>
> DELETE "/orders/{order_id}" Hiermee kan je een order deleten aan de hand van een ordernummer.<br>
> GET "/products" Dit laat alle mogelijke producten zien.<br>
> POST "/products" Hiermee kan je een nieuw product aanmaken.<br>
> POST "/token" Hiermee kan je een token opvragen via bepaalde inloggegevens, deze token kan je gebruiken om bepaalde requests te doen.<br>
> GET "/users/me" Dit laat alle data zien van de gebruiken die is ingelogd via de token.<br>

## Links
* API Links
    * [API Repository](https://github.com/ArneVangheel/API-Eindproject)
    * [Hosted API](https://api-eindproject-arnevangheel.cloud.okteto.net/)
* Front-End Links
    * [Front-End Repository](https://github.com/ArneVangheel/website-eindproject)
    * [Hosted Front-End ](https://api-eindproject.netlify.app/)
## Postman (API Testing)


## OpenAPI Docs Screenshots


## Website


