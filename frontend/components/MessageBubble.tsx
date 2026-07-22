import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

interface Props {
  role: "user" | "assistant";
  text: string;
}

export default function MessageBubble({
  role,
  text,
}: Props) {
  const isUser = role === "user";

  return (
    <div
      className={`mb-6 flex ${
        isUser
          ? "justify-end"
          : "justify-start"
      }`}
    >
      <div
        className={`max-w-3xl rounded-2xl px-5 py-4 shadow ${
          isUser
            ? "bg-blue-600 text-white"
            : "bg-gray-100 text-black"
        }`}
      >
        <div className="mb-2 text-xs font-bold uppercase opacity-70">
          {isUser ? "You" : "AI Assistant"}
        </div>

        {isUser ? (
          <p className="whitespace-pre-wrap">
            {text}
          </p>
        ) : (
          <ReactMarkdown remarkPlugins={[remarkGfm]}>
            {text}
          </ReactMarkdown>
        )}
      </div>
    </div>
  );
}