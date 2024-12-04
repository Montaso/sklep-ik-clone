package com.example;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.safari.SafariDriver;

import com.example.login.LoginHandle;
import com.example.login.RegisterHandle;

public class Main {
    public static void main(String[] args) throws InterruptedException{
        WebDriver driver = new SafariDriver();
        driver.get("https://localhost:8080");
        driver.manage().window().maximize();

        //new RegisterHandle(driver).run();
        new LoginHandle(driver).run();
        Thread.sleep(5000);

        //System.out.println("Entering AddToCart operation");
        new AddToCartHandle(driver).run();
        Thread.sleep(5000);

        new CartRemoveHandle(driver).run();
        Thread.sleep(5000);

        new BuyHandle(driver).run();
        Thread.sleep(2000);
        
        new CheckStatusHandle(driver).run();
        //Thread.sleep(5000);

        driver.quit();
    }
}