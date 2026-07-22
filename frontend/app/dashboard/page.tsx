"use client";

import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";
import ChatWindow from "@/components/ChatWindow";

export default function Dashboard() {
  return (
    <div className="flex h-screen flex-col">
      <Navbar />

      <div className="flex flex-1">
        <Sidebar />

        <ChatWindow />
      </div>
    </div>
  );
}