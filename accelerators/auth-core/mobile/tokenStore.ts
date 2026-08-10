/**
 * Session-token storage.
 *
 * SecureStore (iOS Keychain / Android Keystore) — deliberately NOT
 * AsyncStorage. AsyncStorage is unencrypted plain text on disk, readable
 * from a device backup or any process with filesystem access. If your app
 * handles any data whose leak has a real blast radius (accounts, PII,
 * anything comparable to a session cookie), a leaked session token is a
 * live credential in someone else's hands. The distinction is a real
 * vulnerability, not a preference.
 *
 * A mobile binary can hold no secrets of its own — there is no API key or
 * client secret here. The only credential on-device is the user's own
 * session token, obtained by their own login, revocable server-side via
 * the accelerator's session-management endpoints (see `sessions.py`).
 *
 * Harvested from `little-milestones/dev/mobile/src/auth/tokenStore.ts`
 * (F18 mobile increment).
 */
import { Platform } from 'react-native';
import * as SecureStore from 'expo-secure-store';

const TOKEN_KEY = 'app.session.token'; // adopting project: namespace this key

/**
 * Web fallback — DEV PREVIEW ONLY.
 *
 * SecureStore has no web implementation (there is no Keychain in a browser).
 * Expo Web is a debugging convenience here, not a supported client:
 * localStorage is plain text and offers none of the at-rest protection the
 * native path relies on. Never point this at real production data — use
 * synthetic/test accounts only.
 */
const isWeb = Platform.OS === 'web';

const webStore = {
  set(k: string, v: string) {
    if (typeof localStorage !== 'undefined') localStorage.setItem(k, v);
  },
  get(k: string): string | null {
    return typeof localStorage !== 'undefined' ? localStorage.getItem(k) : null;
  },
  remove(k: string) {
    if (typeof localStorage !== 'undefined') localStorage.removeItem(k);
  },
};

export async function saveToken(token: string): Promise<void> {
  if (isWeb) return webStore.set(TOKEN_KEY, token);
  await SecureStore.setItemAsync(TOKEN_KEY, token, {
    // WHEN_UNLOCKED_THIS_DEVICE_ONLY: keeps the token out of encrypted
    // backups and out of Keychain sync, so a restore onto a new device
    // means re-login rather than a silently migrated session.
    keychainAccessible: SecureStore.WHEN_UNLOCKED_THIS_DEVICE_ONLY,
  });
}

export async function loadToken(): Promise<string | null> {
  if (isWeb) return webStore.get(TOKEN_KEY);
  try {
    return await SecureStore.getItemAsync(TOKEN_KEY);
  } catch {
    // A corrupt/unreadable keychain entry must not brick the app — treat it
    // as signed-out and let the user log in again.
    return null;
  }
}

export async function clearToken(): Promise<void> {
  if (isWeb) return webStore.remove(TOKEN_KEY);
  try {
    await SecureStore.deleteItemAsync(TOKEN_KEY);
  } catch {
    // Already gone is success for our purposes.
  }
}
