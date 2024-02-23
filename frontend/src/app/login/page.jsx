"use client";
import React, { useEffect, useState } from "react";
import styles from "./loginPage.module.css";
import { useRouter } from "next/navigation";
import { Finlandica } from "next/font/google";
import Image from "next/image";
import axios from "axios";
const API_URL = "http://127.0.0.1:5000";

const postData = async (email, password) => {
  const res = await axios.post(
    API_URL + "/sign_in",
    {
      email: email,
      password: password,
    },
    { withCredentials: true }
  );

  if (!res.status === 200) {
    throw new Error("Faild");
  }

  return res.data;
};

export default function LoginPage() {
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();

  const router = useRouter();

  const oauthClickHandler = () => {
    router.push(API_URL + "/authenticate");
  };

  const handleSignIn = async () => {
    const resp = await postData(email, password);
    if (resp.status === "ok") {
      window.location.href = 'http://127.0.0.1:3000';
    }
  };

  const signUpClickHandler = () => {
    router.push("/sign_up");
  };
  return (
    <div className={styles.container}>
      <div className={styles.wrapper}>
        <div
          className={styles.socialButton}
          onClick={() => oauthClickHandler()}
        >
          <Image
            className={styles.googleIcon}
            src="/google.png"
            alt="google"
            width={20}
            height={20}
          />
          Sign in with Google
        </div>
        <input
          className={styles.socialButton}
          type="email"
          placeholder="example@gmail.com"
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          className={styles.socialButton}
          type="password"
          placeholder="Password..."
          onChange={(e) => setPassword(e.target.value)}
        />
        <button
          disabled={!email || !password}
          className={styles.socialButton}
          onClick={() => handleSignIn()}
        >
          Sign In
        </button>
        <button
          className={styles.socialButton}
          onClick={() => signUpClickHandler()}
        >
          Sign Up
        </button>
      </div>
    </div>
  );
}
