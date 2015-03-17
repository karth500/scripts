package com.ramakk;

/**
 * Created by ramakk on 2/19/15.
 */
public class ProviderImpl implements GetSomething<String> {

    @Override
    public String get() {
        System.out.println("Returning something beautiful");
        return "awesome!";
    }
}
