import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TaskListsComponent } from './task-lists/task-lists.component';
import { TaskListDetailComponent } from './task-list-detail/task-list-detail.component';
import { TaskListTasksComponent } from './task-list-tasks/task-list-tasks.component';
import { TaskDetailComponent } from './task-detail/task-detail.component';
import { ProviderService } from './shared/services/provider.service';
import { HttpClientModule } from '@angular/common/http';
import { BaseComponent } from './base/base.component';

@NgModule({
  declarations: [
    AppComponent,
    TaskListsComponent,
    TaskListDetailComponent,
    TaskListTasksComponent,
    TaskDetailComponent,
    BaseComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [
    ProviderService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
