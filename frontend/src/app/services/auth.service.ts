import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  httpHeaders = new HttpHeaders({ 'Content-Type': 'application/json' });
  constructor(private http: HttpClient) { }

  register(body: JSON) {
    return this.http.post('http://127.0.0.1:8000/auth/users/', body, { headers: this.httpHeaders, withCredentials: true })
  }

  login(body: JSON) {
    return this.http.post('http://127.0.0.1:8000/auth/jwt/create/', body, { headers: this.httpHeaders, withCredentials: true })
  }

  logout() {
    return this.http.post('http://127.0.0.1:8000/logout/', { headers: this.httpHeaders, withCredentials: true })
  }

  getUser() {
    return this.http.get('http://127.0.0.1:8000/auth/users/me/', { headers: this.httpHeaders, withCredentials: true })
  }

  forgotPassword(body: JSON) {
    return this.http.post('http://127.0.0.1:8000/auth/users/reset_password/', body, { headers: this.httpHeaders, withCredentials: true })
  } 
}