export default function Navbar() {
  return (
    <header className="flex h-16 items-center justify-between border-b bg-white px-8 shadow-sm">
      <h1 className="text-2xl font-bold">
        🤖 AI Knowledge Assistant
      </h1>

      <button className="rounded-lg bg-red-500 px-4 py-2 text-white hover:bg-red-600">
        Logout
      </button>
    </header>
  );
}