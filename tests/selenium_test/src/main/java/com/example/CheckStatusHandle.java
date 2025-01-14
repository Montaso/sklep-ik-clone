package com.example;

import org.openqa.selenium.WebDriver;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter @Setter
@AllArgsConstructor
public class CheckStatusHandle {

    private final WebDriver driver;
    private final String statusLink = "https://localhost:19323/historia-zamowien";

    public void run() throws InterruptedException{
        driver.get(statusLink);
        Thread.sleep(5000);

        
    }


}
