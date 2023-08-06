import { JwksValidationHandler, OAuthService } from "angular-oauth2-oidc";
import { authCodeFlowConfig } from "./cognito.model";
import { Component, OnInit } from '@angular/core';

export class AppComponent implements OnInit {
    title = 'swift-health';
    isAuthenticated: boolean = false;

    constructor( private oauthService: OAuthService ) {
        this.configure();
    }

    private configure () {
        this.oauthService.configure(authCodeFlowConfig);
        this.oauthService.tokenValidationHandler = 
            new JwksValidationHandler();
        this.oauthService.loadDiscoveryDocumentAndTryLogin();
        this.oauthService.setupAutomaticSilentRefresh();
    }

    ngOnInit() {
        //Called after the constructor, initializing input properties, and the first call to ngOnChanges.
          //Add 'implements OnInit' to the class.
        }
}