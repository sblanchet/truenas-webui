import { createAction, props } from '@ngrx/store';
import { Preferences, TableDisplayedColumns } from 'app/interfaces/preferences.interface';

export const preferencesLoaded = createAction('[Preferences API] Loaded', props<{ preferences: Preferences }>());
export const noPreferencesFound = createAction('[Preferences API] No Preferences Found');

// TODO: These actions will be moved elsewhere in the future
export const themeNotFound = createAction('[Preferences] Theme Not Found');
export const preferencesFormSubmitted = createAction('[Preferences] Form Submitted', props<{ formValues: {
  userTheme: string;
  preferIconsOnly: boolean;
  allowPwToggle: boolean;
  retroLogo: boolean;
  tableDisplayedColumns?: TableDisplayedColumns[];
}; }>());
export const preferencesReset = createAction('[Preferences] Reset');
export const preferredColumnsUpdated = createAction(
  '[Preferences] Preferred Columns Updated',
  props<{ columns: TableDisplayedColumns[] }>(),
);
export const localizationFormSubmitted = createAction('[Preferences] Localization Form Submitted', props<{
  dateFormat: string;
  timeFormat: string;
}>());

export const oneTimeBuiltinUsersMessageShown = createAction('[Preferences] One Time Builtin Users Message Shown');
export const oneTimeBuiltinGroupsMessageShown = createAction('[Preferences] One Time Builtin Groups Message Shown');
export const builtinUsersToggled = createAction('[Preferences] Builtin Users Toggled');
export const builtinGroupsToggled = createAction('[Preferences] Builtin Groups Toggled');