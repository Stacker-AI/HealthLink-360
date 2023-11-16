import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  
  accessToken = "";

  constructor(private http: HttpClient) { }

  register(body: JSON) {
    return this.http.post('http://127.0.0.1:8000/api/registration/', body)
  }

  login(body: JSON) {
    return this.http.post('http://127.0.0.1:8000/api/login/', body, { withCredentials: true })
      .pipe(
        tap((response: any) => {
          this.accessToken = response.key;
          console.log(this.accessToken);
          localStorage.setItem('accessToken', this.accessToken);
        })
      );
  }

  logout() {
    return this.http.post('http://127.0.0.1/api/logout/', {}, { withCredentials: true })
      .pipe(
        tap(() => {
          this.accessToken = '';
          localStorage.removeItem('accessToken');
        })
      );
  }

  isLoggedIn(): boolean {
    this.accessToken = localStorage.getItem('accessToken') || '';
    const isLoggedIn = Boolean(this.accessToken);
    return isLoggedIn;
  }
}