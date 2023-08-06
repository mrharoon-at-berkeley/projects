

OnInit(): void {
    this.tokenSubscription = this.oauthSerivce.events.pipe(
        filter(e => e.type === 'token_received')).subscribe(
            e => {
                this.accessToken = this.oauthService.getAccessToken();
            }
        )
}

function OnInit() {
    throw new Error("Function not implemented.");
}
