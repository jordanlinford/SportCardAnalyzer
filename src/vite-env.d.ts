/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_FIREBASE_API_KEY: string;
  readonly VITE_FIREBASE_AUTH_DOMAIN: string;
  readonly VITE_FIREBASE_PROJECT_ID: string;
  readonly VITE_FIREBASE_STORAGE_BUCKET: string;
  readonly VITE_FIREBASE_MESSAGING_SENDER_ID: string;
  readonly VITE_FIREBASE_APP_ID: string;
  readonly VITE_FIREBASE_MEASUREMENT_ID: string;

  readonly VITE_STRIPE_STAR_MONTHLY_PRICE_ID: string;
  readonly VITE_STRIPE_STAR_ANNUAL_PRICE_ID: string;
  readonly VITE_STRIPE_VETERAN_MONTHLY_PRICE_ID: string;
  readonly VITE_STRIPE_VETERAN_ANNUAL_PRICE_ID: string;

  readonly VITE_SCRAPER_API: string;
  readonly MODE: 'development' | 'production';
  // Add other environment variables here as needed
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
} 