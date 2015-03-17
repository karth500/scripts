package com.ramakk;

public class Main {

    public static void main(String[] args) {
	// write your code here
        final PriorityProviderImpl p = new PriorityProviderImpl();
        System.out.println(p.get());
        System.out.println(p.getPriority());
    }
}
