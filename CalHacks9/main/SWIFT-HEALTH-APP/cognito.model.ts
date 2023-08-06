
import { AuthConfig } from 'angular-oauth2-oidc';

export const authCodeFlowConfig: AuthConfig = {
  // Url of ID provider
  issuer: 'https://cognito-idp.us-east-2.amazonaws.com/us-east-2_7h1zsNQjM',

  redirectUri: 'https://portal.events.isccloud.io/callback',

  // SPA's id (registered with this id at auth-server)
  clientId: '19et3nrqpir5ldvhpm5e6rb2eo',
  strictDiscoveryDocumentValidation: false,
  responseType: 'token',
  scope: 'open profile launch/patient',
  showDebugInformation: true,
};