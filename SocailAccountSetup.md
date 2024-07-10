# Social Account Setup

This guide provides step-by-step instructions for obtaining the Client ID and Secret Key from GitHub, Google, and Facebook to integrate social authentication into your Django application.

## GitHub

### Step 1: Create a New OAuth App

1. **Go to GitHub Developer Settings**:
   - Open your web browser and navigate to [GitHub Developer Settings](https://github.com/settings/developers).
   
2. **Register a New OAuth Application**:
   - Click on **New OAuth App**.

3. **Application Details**:
   - **Application Name**: Enter the name of your application.
   - **Homepage URL**: Enter the homepage URL of your application, e.g., `http://127.0.0.1:8000/`.
   - **Authorization Callback URL**: Enter the callback URL, e.g., `http://127.0.0.1:8000/auth/complete/github/`.

4. **Register Application**:
   - Click the **Register application** button.

5. **Retrieve Client ID and Client Secret**:
   - After registering, you will be redirected to the application page where you can find your **Client ID** and **Client Secret**. 

## Google

### Step 1: Create a New Project

1. **Go to Google Cloud Console**:
   - Open your web browser and navigate to [Google Cloud Console](https://console.developers.google.com/).

2. **Create a New Project**:
   - Click on the project dropdown at the top and select **New Project**.
   - Enter a project name and click **Create**.

### Step 2: Enable OAuth Consent Screen

1. **OAuth Consent Screen**:
   - Navigate to **APIs & Services** > **OAuth consent screen**.
   - Select **External** and click **Create**.
   - Fill in the required fields and save.

### Step 3: Create OAuth Credentials

1. **Create Credentials**:
   - Go to **APIs & Services** > **Credentials**.
   - Click on **Create Credentials** and select **OAuth 2.0 Client IDs**.

2. **Configure OAuth Consent Screen**:
   - Choose **Web application** as the application type.
   - Name your OAuth 2.0 client.

3. **Authorized Redirect URIs**:
   - Add the authorized redirect URI, e.g., `http://127.0.0.1:8000/auth/complete/google-oauth2/`.

4. **Create**:
   - Click **Create** and you will be provided with your **Client ID** and **Client Secret**.

## Facebook

### Step 1: Create a New App

1. **Go to Facebook for Developers**:
   - Open your web browser and navigate to [Facebook for Developers](https://developers.facebook.com/).

2. **Create App**:
   - Click on **My Apps** in the top right corner and then click **Create App**.
   - Select **For Everything Else** and click **Continue**.

3. **App Details**:
   - Enter your app name and contact email, then click **Create App ID**.

### Step 2: Configure Facebook Login

1. **Set Up Facebook Login**:
   - After creating the app, you will be redirected to the app dashboard.
   - In the left sidebar, select **Add Product** and find **Facebook Login**. Click **Set Up**.

2. **Settings**:
   - Navigate to **Facebook Login** > **Settings**.
   - In the **Valid OAuth Redirect URIs** field, add the redirect URI, e.g., `http://127.0.0.1:8000/auth/complete/facebook/`.

3. **Save Changes**:
   - Click **Save Changes**.

### Step 3: Retrieve Client ID and Client Secret

1. **Basic Settings**:
   - Go to **Settings** > **Basic**.
   - Here you can find your **App ID** and **App Secret**.

## Adding Credentials to Your Django Application

After obtaining the Client ID and Secret Key from GitHub, Google, and Facebook, add them to your Django settings or environment variables.

```python
# settings.py

# GitHub OAuth2
SOCIAL_AUTH_GITHUB_KEY = 'your-github-client-id'
SOCIAL_AUTH_GITHUB_SECRET = 'your-github-client-secret'

# Google OAuth2
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your-google-client-id'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your-google-client-secret'

# Facebook OAuth2
SOCIAL_AUTH_FACEBOOK_KEY = 'your-facebook-app-id'
SOCIAL_AUTH_FACEBOOK_SECRET = 'your-facebook-app-secret'
