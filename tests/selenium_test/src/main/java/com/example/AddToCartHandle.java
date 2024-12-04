package com.example;

import java.util.List;
import java.util.Random;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.safari.SafariDriver;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter @Setter
public class AddToCartHandle {

    private WebDriver driver;
    private final String category1Link = "https://localhost:8080/23-AIR-shop";
    private final String divFullClass = "js-product product col-xs-12 col-sm-6 col-xl-4";

    private final String quantityId = "quantity_wanted";
    private final String cartClass = "add-to-cart";

    private final String[] productLinks = {"https://localhost:8080/AIR-shop/3012-https-wwwsklep-ikpl-produkt-drops-air-05-mix-braz-.html",
                                        "https://localhost:8080/AIR-shop/3016-https-wwwsklep-ikpl-produkt-drops-air-09-mix-granatowy-.html",
                                        "https://localhost:8080/AIR-shop/3019-https-wwwsklep-ikpl-produkt-drops-air-10-mix-mgla-.html",
                                        "https://localhost:8080/AIR-shop/3021-https-wwwsklep-ikpl-produkt-drops-air-13-mix-pomaranczowy-.html",
                                        "https://localhost:8080/AIR-shop/3023-https-wwwsklep-ikpl-produkt-drops-air-15-mix-fioletowa-mgielka-.html",
                                        "https://localhost:8080/DAISY-shop/3450-https-wwwsklep-ikpl-produkt-drops-daisy-01-ecru-.html",
                                        "https://localhost:8080/DAISY-shop/3454-https-wwwsklep-ikpl-produkt-drops-daisy-06-pudrowy-roz-.html",
                                        "https://localhost:8080/DAISY-shop/3456-https-wwwsklep-ikpl-produkt-drops-daisy-07-slodka-orchidea-.html",
                                        "https://localhost:8080/ARROYO-shop/4508-https-wwwsklep-ikpl-produkt-malabrigo-arroyo-005-aniversario-0000-.html",
                                        "https://localhost:8080/karty-podarunkowe-shop/5676-https-wwwsklep-ikpl-produkt-pudelko-z-karta-upominkowa-200-zl-gratis-.html"};

    private final String searchKeyword = "abc";

    public AddToCartHandle(WebDriver driver) {
        this.driver = driver;
    }
    
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
                driver.findElement(By.id(quantityId)).sendKeys(Integer.toString(random.nextInt(stock)/2));

                driver.findElement(By.className(cartClass)).click();
            }
        }

        driver.get("https://localhost:8080");
        driver.findElement(By.name("s")).sendKeys(searchKeyword + "\n");
        Thread.sleep(1000);
        driver.findElement(By.className("quick-view")).click();
        Thread.sleep(1000);
        driver.findElement(By.className("add-to-cart")).click();

        //driver.get("https://localhost:8080/koszyk?action=show");

    }

}
