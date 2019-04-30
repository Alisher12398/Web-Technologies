import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TaskListsComponent } from './task-lists/task-lists.component';
import { AppComponent } from './app.component';
import { TaskListDetailComponent } from './task-list-detail/task-list-detail.component';
import { TaskListTasksComponent } from './task-list-tasks/task-list-tasks.component';
import { TaskDetailComponent } from './task-detail/task-detail.component';
import { BaseComponent } from './base/base.component';
import { RegisterComponent } from './auth/register/register.component';
import { LoginComponent } from './auth/login/login.component';

const routes: Routes = [
  {path: '', component: BaseComponent},
  {path: 'task_lists', component: TaskListsComponent},
  {path: 'task_lists/:id', component: TaskListDetailComponent},
  {path: 'task_lists/:id/tasks', component: TaskListTasksComponent},
  {path: 'tasks/:id', component: TaskDetailComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'login', component: LoginComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
