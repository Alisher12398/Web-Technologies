import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService extends MainService {

  constructor(http: HttpClient) { 
    super(http)
  }

  isAuthenticated(): boolean {
    return !!localStorage.getItem('token');
  }

  register(username: any, password: any): void{
    this.post('http://localhost:8000/api/register/', {
      username: username,
      password: password
    }).then(res => {
      localStorage.setItem('token', res.token);
    });
  }

  login(username: any, password: any): void{
    this.post('http://localhost:8000/api/login/', {
      username: username,
      password: password
    }).then(res => {
      localStorage.setItem('token', res.token);

      console.log(res)
    });
  }

  logout(): void {
    this.post('http://localhost:8000/api/logout/', {}).then(() => {
      localStorage.clear();
    // this.token = ''
    });
  }
}
