import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { ITaskList } from '../shared/models';
import { Location } from '@angular/common';

@Component({
  selector: 'app-task-lists',
  templateUrl: './task-lists.component.html',
  styleUrls: ['./task-lists.component.sass']
})
export class TaskListsComponent implements OnInit {

  public taskLists: ITaskList[] = [];

  constructor(
    private provider: ProviderService,
    private location: Location
    ) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.taskLists = res;
    })
  }

  navigateBack(){
    this.location.back()
  }

  // sendId(id: number){
  //   this.provider.sendMessage.emit(id+"")
  // }

}
