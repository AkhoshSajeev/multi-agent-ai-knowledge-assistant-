"use client";
import { useRef, useEffect } from "react";
import { useState } from "react";
import api from "@/lib/api";
import MessageBubble from "@/components/MessageBubble";
interface Message {
  role: "user" | "assistant";
  text: string;
}

export default function ChatWindow() {
  const [question, setQuestion] = useState("");

  const [messages, setMessages] = useState<Message[]>([]);

  const [loading, setLoading] = useState(false);

  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
  bottomRef.current?.scrollIntoView({
    behavior: "smooth",
  });
}, [messages, loading]);

  async function sendQuestion() {

    if (!question.trim()) return;

    const userMessage: Message = {
      role: "user",
      text: question,
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {

      const response = await api.post(
        "/chat",
        {
          question,
        }
      );

      const aiMessage: Message = {
        role: "assistant",
        text: response.data.answer,
      };

      setMessages((prev) => [...prev, aiMessage]);

    } catch (error) {

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "Something went wrong.",
        },
      ]);

    } finally {

      setLoading(false);

      setQuestion("");

    }

  }

  return (
    <main className="flex flex-1 flex-col bg-white">

      <div className="flex-1 overflow-y-auto p-8">

       {messages.map((message, index) => (
  <MessageBubble
    key={index}
    role={message.role}
    text={message.text}
  />
))}
        {loading && (

         <div className="mb-4">
  <div className="inline-block rounded-xl bg-gray-100 px-4 py-3">
    🤖 Thinking...
  </div>
</div>

        )}
        <div ref={bottomRef} />

      </div>

      <div className="border-t p-5">

        <div className="flex gap-3">

          <input
className="flex-1 rounded-xl border border-gray-300 p-4 outline-none focus:border-blue-500"            placeholder="Ask about your documents..."
            value={question}
            onChange={(e) =>
              setQuestion(e.target.value)
            }
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                sendQuestion();
              }
            }}
          />

         <button
  onClick={sendQuestion}
  disabled={loading}
  className={`rounded-xl px-6 py-3 text-white transition ${
    loading
      ? "cursor-not-allowed bg-gray-400"
      : "bg-blue-600 hover:bg-blue-700"
  }`}
>
  {loading ? "Thinking..." : "Send"}
</button>

        </div>

      </div>

    </main>
  );
}
