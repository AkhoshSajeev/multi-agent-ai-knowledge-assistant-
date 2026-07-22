"use client";

import api from "@/lib/api";

interface Props {
  documentId: number;
  onDeleteSuccess: () => void;
}

export default function DeleteButton({
  documentId,
  onDeleteSuccess,
}: Props) {
  async function deleteDocument() {
    const confirmed = window.confirm(
      "Are you sure you want to delete this document?"
    );

    if (!confirmed) return;

    try {
      await api.delete(`/documents/${documentId}`);

      onDeleteSuccess();

    } catch (error) {
      console.error(error);
      alert("Failed to delete document");
    }
  }

  return (
    <button
      onClick={deleteDocument}
      className="rounded p-2 text-red-600 hover:bg-red-100"
      title="Delete"
    >
      🗑️
    </button>
  );
}