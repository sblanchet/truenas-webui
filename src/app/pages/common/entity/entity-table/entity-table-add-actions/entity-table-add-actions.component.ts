import {
  Component, ElementRef, Input, ViewChild, OnInit, AfterViewInit,
} from '@angular/core';
import { UntilDestroy, untilDestroyed } from '@ngneat/until-destroy';
import { TranslateService } from '@ngx-translate/core';
import { fromEvent as observableFromEvent } from 'rxjs';
import { debounceTime, distinctUntilChanged } from 'rxjs/operators';
import { GlobalAction } from 'app/interfaces/global-action.interface';
import { EntityTableAddActionsConfig } from 'app/pages/common/entity/entity-table/entity-table-add-actions/entity-table-add-actions-config.interface';
import { EntityTableComponent } from 'app/pages/common/entity/entity-table/entity-table.component';

@UntilDestroy()
@Component({
  selector: 'app-entity-table-add-actions',
  templateUrl: './entity-table-add-actions.component.html',
})
export class EntityTableAddActionsComponent implements GlobalAction, OnInit, AfterViewInit {
  @ViewChild('filter', { static: false }) filter: ElementRef;
  @Input('entity') entity: EntityTableComponent;
  conf: EntityTableAddActionsConfig;

  actions: any[];
  menuTriggerMessage = 'Click for options';

  spin = true;
  direction = 'left';
  animationMode = 'fling';

  get totalActions(): number {
    const addAction = this.entity.conf.route_add ? 1 : this.entity.conf.doAdd ? 1 : 0;
    return this.actions.length + addAction;
  }

  constructor(protected translate: TranslateService) { }

  ngOnInit(): void {
    this.actions = this.entity.getAddActions();
  }

  ngAfterViewInit(): void {
    this.filterInit();
  }

  applyConfig(entity: EntityTableComponent): void {
    this.entity = entity;
    this.conf = entity.conf;
    this.filterInit();
  }

  // Set the filter event handler.
  filterInit(): void {
    if (this.filter && this.entity) {
      observableFromEvent(this.filter.nativeElement, 'keyup').pipe(
        debounceTime(150),
        distinctUntilChanged(),
      )
        .pipe(untilDestroyed(this)).subscribe(() => {
          this.entity.filter(this.filter.nativeElement.value);
        });
    }
  }
}