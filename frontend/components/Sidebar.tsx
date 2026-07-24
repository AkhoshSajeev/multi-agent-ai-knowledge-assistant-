"use client";

import { useEffect, useState } from "react";
import DeleteButton from "@/components/DeleteButton";
import api from "@/lib/api";
import UploadButton from "@/components/UploadButton";
import { Document } from "@/types/document";

export default function Sidebar() {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
  loadDocuments();

  const interval = setInterval(() => {
    loadDocuments();
  }, 3000);

  return () => clearInterval(interval);
}, []);

  async function loadDocuments() {
    try {
      setLoading(true);

      const response = await api.get("/documents");

      setDocuments(response.data);

    } catch (error) {
      console.error("Failed to load documents", error);
    } finally {
      setLoading(false);
    }
  }

  return (
    <aside className="w-72 border-r bg-gray-50 p-5">

      <h2 className="mb-5 text-xl font-semibold">
        📄 Documents
      </h2>

      <UploadButton
        onUploadSuccess={loadDocuments}
      />

      {loading ? (
        <p>Loading...</p>

      ) : documents.length === 0 ? (

        <p className="text-gray-500">
          No documents uploaded
        </p>

      ) : (

        <div className="space-y-3">

          {documents.map((doc) => (

  <div
    key={doc.id}
    className="flex items-center justify-between rounded-lg border bg-white p-3 shadow-sm"
  >

   <div className="flex-1 min-w-0">

  <h3 className="font-medium truncate">
    {doc.original_filename}
  </h3>

  <p
    className={`text-sm ${
      doc.status === "completed"
        ? "text-green-600"
        : doc.status === "processing"
        ? "text-yellow-600"
        : "text-red-600"
    }`}
  >
    {doc.status}
  </p>

</div>

    <DeleteButton
      documentId={doc.id}
      onDeleteSuccess={loadDocuments}
    />

  </div>

))}

        </div>

      )}

    </aside>
  );
}