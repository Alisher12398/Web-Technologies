import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TaskListTasksComponent } from './task-list-tasks.component';

describe('TaskListTasksComponent', () => {
  let component: TaskListTasksComponent;
  let fixture: ComponentFixture<TaskListTasksComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TaskListTasksComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TaskListTasksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
