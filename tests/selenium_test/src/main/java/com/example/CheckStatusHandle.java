package com.example;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.safari.SafariDriver;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter @Setter
public class CheckStatusHandle {

    private WebDriver driver;
    private final String statusLink = "https://localhost:8080/historia-zamowien";
    
    public CheckStatusHandle(WebDriver driver) {
        this.driver = driver;
    }

    public void run() throws InterruptedException{
        driver.get(statusLink);
        Thread.sleep(5000);

        
    }


}
