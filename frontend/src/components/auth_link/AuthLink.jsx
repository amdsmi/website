"use client";
import React, { useEffect, useState } from "react";
import styles from "./authLink.module.css";
import Link from "next/link";
import axios from "axios";
import Cookies from "js-cookie";
const API_URL = "http://127.0.0.1:5000";


export default function AuthLink() {
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get(API_URL + "/", { withCredentials: true }).then((res) => {
      setLoading(false);
      setData(res.data.status);
    });
  }, [data]);

  const deleteCookie = () => {
    Cookies.remove("user_id");
    Cookies.remove("user_token");
    location.reload();
  };

  console.log(data);

  return (
    <>
      {data === "unauthenticated" ? (
        <Link className={styles.link} href="/login">
          Sgin In/Up
        </Link>
      ) : (
        <>
          <Link className={styles.link} href="/write">
            Write
          </Link>
          <span className={styles.link} onClick={deleteCookie}>
            Logout
          </span>
        </>
      )}
      <div className={styles.burger} onClick={() => setOpen(!open)}>
        <div className={styles.line}></div>
        <div className={styles.line}></div>
        <div className={styles.line}></div>
      </div>
      {open && (
        <div className={styles.responsiveMenu}>
          <Link href="/">HomePage</Link>
          <Link href="/">Applications</Link>
          <Link href="/">About</Link>
          {data === "unauthenticated" ? (
            <Link href="/login">Login</Link>
          ) : (
            <>
              <Link href="/Write">Write</Link>
              <span className={styles.link}>Logout</span>
            </>
          )}
        </div>
      )}
    </>
  );
}

function MyComponent() {
  const [cookiesDeleted, setCookiesDeleted] = useState(false);

  const handleLogout = () => {
    document.cookie =
      "user_id" + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    document.cookie =
      "user_token" + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    setCookiesDeleted(true);
  };

  return (
    <div>
      {cookiesDeleted ? (
        <p>Cookies deleted successfully.</p>
      ) : (
        <button onClick={handleLogout}>Logout</button>
      )}
    </div>
  );
}
