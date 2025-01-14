package com.example;

import java.util.List;
import java.util.Random;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter @Setter
@AllArgsConstructor
public class AddToCartHandle {

    private WebDriver driver;
    private final String category1Link = "https://localhost:19323/520-MIDARA-shop";
    private final String divFullClass = "js-product product col-xs-12 col-sm-6 col-xl-4";

    private final String quantityId = "quantity_wanted";
    private final String cartClass = "add-to-cart";

    private final String[] productLinks = {"https://localhost:19323/AIR-shop/7946-https-wwwsklep-ikpl-produkt-drops-air-19-zielony-lesny-.html",
                                        "https://localhost:19323/AIR-shop/7942-https-wwwsklep-ikpl-produkt-drops-air-13-mix-pomaranczowy-.html",
                                        "https://localhost:19323/baby-merino-shop/7984-https-wwwsklep-ikpl-produkt-drops-baby-merino-11-blekitny-stalowy-.html",
                                        "https://localhost:19323/baby-merino-shop/7986-https-wwwsklep-ikpl-produkt-drops-baby-merino-16-czerwony-.html",
                                        "https://localhost:19323/DAISY-shop/8054-https-wwwsklep-ikpl-produkt-drops-daisy-12-karmel-.html",
                                        "https://localhost:19323/DAISY-shop/8053-https-wwwsklep-ikpl-produkt-drops-daisy-10-blekitny-.html",
                                        "https://localhost:19323/PARIS-shop/8186-https-wwwsklep-ikpl-produkt-drops-paris-11-zielony-opal-.html",
                                        "https://localhost:19323/PARIS-shop/8191-https-wwwsklep-ikpl-produkt-drops-paris-17-ecru-.html",
                                        "https://localhost:19323/GUZIKI-shop/8841-https-wwwsklep-ikpl-produkt-drops-guzik-513-cedr-15mm-.html",
                                        "https://localhost:19323/nozyczki-shop/8875-https-wwwsklep-ikpl-produkt-ostre-nozyczki-stork-srebrne-115-cm-.html"};

    private final String searchKeyword = "abc";
    public void run() throws InterruptedException{
        // driver.get(category1Link);
        // Random random = new Random();
        // int remainingToAdd = 5;
        // List<WebElement> productList = driver.findElements(By.className("product-thumbnail"));
        // //driver.findElement(By.className("add-to-cart")).click();
        // for(WebElement product : productList) {
        //     product.click();
        //     int stock = 0;
        //     List<WebElement> element = driver.findElements(By.cssSelector("span[data-stock]"));
            
        //     if(element.size() > 0)
        //     {
        //         stock = Integer.parseInt(element.get(0).getAttribute("data-stock"));
        //         driver.findElement(By.id(quantityId)).sendKeys(Integer.toString(random.nextInt(stock)));

        //         driver.findElement(By.className(cartClass)).click();
        //         remainingToAdd--;
        //     }
        // }
        Random random = new Random();
        for(String link : productLinks) {
            driver.get(link);
            List<WebElement> element = driver.findElements(By.cssSelector("span[data-stock]"));
            int stock;
            if(element.size() > 0)
            {
                stock = Integer.parseInt(element.get(0).getAttribute("data-stock"));
                //driver.findElement(By.id(quantityId)).sendKeys(Integer.toString(random.nextInt(stock)/2+1));
                for(int i = 0; i < random.nextInt(stock)/2; i++) {
                    driver.findElement(By.className("touchspin-up")).click();
                }
                

                driver.findElement(By.className(cartClass)).click();
            }
        }

        Thread.sleep(2000);
        driver.get("https://localhost:19323");
        driver.findElement(By.name("s")).sendKeys(searchKeyword + "\n");
        Thread.sleep(1000);
        driver.findElement(By.className("product-thumbnail")).click();
        Thread.sleep(5000);
        driver.findElement(By.className("add-to-cart")).click();

        //driver.get("https://localhost:8080/koszyk?action=show");

    }

}
