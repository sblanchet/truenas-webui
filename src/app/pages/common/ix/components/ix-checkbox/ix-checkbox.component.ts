import {
  ChangeDetectionStrategy, Component, Input,
} from '@angular/core';
import {
  ControlValueAccessor, NgControl,
} from '@angular/forms';
import { UntilDestroy } from '@ngneat/until-destroy';

@UntilDestroy()
@Component({
  selector: 'ix-checkbox',
  styleUrls: ['./ix-checkbox.component.scss'],
  templateUrl: './ix-checkbox.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class IxCheckboxComponent implements ControlValueAccessor {
  @Input() label: string;
  @Input() hint: string;
  @Input() tooltip: string;
  @Input() required: boolean;

  isDisabled = false;
  value: boolean;

  constructor(
    public controlDirective: NgControl,
  ) {
    this.controlDirective.valueAccessor = this;
  }

  onChange: (value: boolean) => void = (): void => {};
  onTouch: () => void = (): void => {};

  writeValue(value: boolean): void {
    this.value = value;
  }

  registerOnChange(onChange: (value: boolean) => void): void {
    this.onChange = onChange;
  }

  registerOnTouched(onTouched: () => void): void {
    this.onTouch = onTouched;
  }

  setDisabledState?(isDisabled: boolean): void {
    this.isDisabled = isDisabled;
  }
}