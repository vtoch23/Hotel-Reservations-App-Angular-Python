import { Injectable } from '@angular/core';
import { Reservation } from '../models/reservation';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ReservationService {
  private apiUrl = "http://127.0.0.1:8000";

  constructor(private http: HttpClient){}

  //CRUD

  getReservations(): Observable<Reservation[]> {
    return this.http.get<Reservation[]>(this.apiUrl + '/');
  }

  getReservation(id: string): Observable<Reservation> {
    return this.http.get<Reservation>(this.apiUrl+'/get_reservation/'+id);
  }

  addReservation(reservation: Reservation): Observable<void> {
    let body = new FormData();
    body.append('guestName', reservation.guestName);
    body.append('guestEmail', reservation.guestEmail);
    body.append('checkInDate', JSON.stringify(reservation.checkInDate));
    body.append('checkOutDate', JSON.stringify(reservation.checkOutDate));
    body.append('roomNumber', JSON.stringify(reservation.roomNumber));
    body.append('icon', reservation.icon);
    return this.http.post<void>(this.apiUrl+'/add_reservation', body);
  }

  deleteReservation(id: string): Observable<void> {
    const httpOptions = {
      headers: new HttpHeaders({ 
        'Access-Control-Allow-Origin': '*',
      }),
      body: {'id': id}
    };
    return this.http.delete<void>(this.apiUrl+'/delete_reservation/'+id, httpOptions);
  }

  updateReservation(id: string, reservation: Reservation): Observable<void> {
    let body = new FormData();
    body.append('guestName', reservation.guestName);
    body.append('guestEmail', reservation.guestEmail);
    body.append('checkInDate', JSON.stringify(reservation.checkInDate));
    body.append('checkOutDate', JSON.stringify(reservation.checkOutDate));
    body.append('roomNumber', JSON.stringify(reservation.roomNumber));
    body.append('icon', reservation.icon);
    return this.http.put<void>(this.apiUrl+'/update_reservation/'+id, body);
  } 
}
