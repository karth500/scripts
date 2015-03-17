package com.ramakk;

/**
 * Created by ramakk on 2/19/15.
 */
public class PriorityProviderImpl extends ProviderImpl implements GetPrioritySomething<String> {

    @Override
    public int getPriority() {
        return 0;
    }
}
