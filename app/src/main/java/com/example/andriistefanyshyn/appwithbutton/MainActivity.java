package com.example.andriistefanyshyn.appwithbutton;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private static final String STATE_GREETING = "STATE_GREETING";

    private TextView mHelloTextView;
    private boolean mIsButtonGreeting;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mIsButtonGreeting = false;
        mHelloTextView = (TextView) findViewById(R.id.hello_text);

        Button clickMeButton = (Button) findViewById(R.id.click_me);
        clickMeButton.setOnClickListener(this);
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        outState.putBoolean(STATE_GREETING, mIsButtonGreeting);

        super.onSaveInstanceState(outState);
    }

    @Override
    protected void onRestoreInstanceState(Bundle savedInstanceState) {
        super.onRestoreInstanceState(savedInstanceState);

        mIsButtonGreeting = savedInstanceState.getBoolean(STATE_GREETING);
        setGreetingText();
    }

    @Override
    public void onClick(View v) {
        mIsButtonGreeting = !mIsButtonGreeting;
        setGreetingText();
    }

    private void setGreetingText() {
        if (mIsButtonGreeting) {
            mHelloTextView.setText(R.string.hello_button);
        }
        else {
            mHelloTextView.setText(R.string.hello_android);
        }
    }
}
