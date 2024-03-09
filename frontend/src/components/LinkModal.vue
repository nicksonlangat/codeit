<template>
<TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="closeModal" class="relative z-10">
        <TransitionChild as="template" enter="duration-300 ease-out" enter-from="opacity-0" enter-to="opacity-100" leave="duration-200 ease-in" leave-from="opacity-100" leave-to="opacity-0">
            <div class="fixed inset-0 bg-black/25" />
        </TransitionChild>

        <div class="fixed inset-0 overflow-y-auto">
            <div class="flex min-h-full font-base text-white items-center justify-center p-4 text-center">
                <TransitionChild as="template" enter="duration-300 ease-out" enter-from="opacity-0 scale-95" enter-to="opacity-100 scale-100" leave="duration-200 ease-in" leave-from="opacity-100 scale-100" leave-to="opacity-0 scale-95">
                    <DialogPanel class="w-full max-w-md transform overflow-hidden rounded-2xl bg-[#151515] p-6 text-left align-middle shadow-xl transition-all">
                        <div class="flex items-center justify-between">
                            <h1>Share Link</h1>
                            <span @click="closeModal" class="cursor-pointer hover:bg-[#191919] px-1.5 py-1 rounded-full transition-all duration-300">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
                                </svg>
                            </span>

                        </div>
                        <hr class="border border-neutral-600 mt-5">
                        <div class="mt-5 flex gap-5">
                            <div class="bg-[#191919] w-2/3 py-1.5 rounded-md">
                                <p class="ml-4 text-[#d8fb4e]">{{ data }}</p>
                            </div>
                            <button v-if="!isCopied" @click="copyLink" class="bg-[#167dff] w-1/3 inline-flex gap-2 items-center py-1 px-3 text-xs rounded-lg">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 0 0 2.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 0 0-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75 2.25 2.25 0 0 0-.1-.664m-5.8 0A2.251 2.251 0 0 1 13.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V9.375c0-.621-.504-1.125-1.125-1.125H8.25ZM6.75 12h.008v.008H6.75V12Zm0 3h.008v.008H6.75V15Zm0 3h.008v.008H6.75V18Z" />
                        </svg>

                        Copy link</button>
                        <button v-if="isCopied" class="bg-[#167dff] w-1/3 inline-flex gap-2 items-center py-1 px-3 text-xs rounded-lg">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4 text-primary">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                                </svg>


                        Link Copied</button>
                        </div>
                        <div class="mt-5 flex items-center gap-2">
                            <input type="checkbox" checked disabled class="h-4 rounded-md w-4">
                           <p>Make link accessible to anyone</p>
                        </div>
                        <div class="mt-5 flex gap-5">
                            <div class="bg-[#191919] w-2/3 py-1.5 rounded-md">
                                <p class="ml-4 text-xs text-[#fefefe]">Anyone with link can edit the snippet.</p>
                            </div>
                           
                        </div>
                    </DialogPanel>
                </TransitionChild>
            </div>
        </div>
    </Dialog>
</TransitionRoot>
</template>

<script>
import {
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogPanel,
    DialogTitle,
} from '@headlessui/vue'
export default {
    components: {
        TransitionRoot,
        TransitionChild,
        Dialog,
        DialogPanel,
        DialogTitle,
    },
    data() {
        return {
            isOpen: false,
            data: "",
            isCopied: false
        }
    },
    methods: {
        openModal() {
            this.isOpen = true
        },
        closeModal() {
            this.isOpen = false
        },
        unsecuredCopyToClipboard(text) {
            const textArea = document.createElement("textarea")
            textArea.value = text
            document.body.appendChild(textArea)
            textArea.focus()
            textArea.select()
            try {
                document.execCommand('copy')
            } catch (err) {
                console.error('Unable to copy to clipboard', err)
            }
            document.body.removeChild(textArea)
        },
        copyLink() {
            if (window.isSecureContext && navigator.clipboard) {
                navigator.clipboard.writeText(this.data)
            } else {
                this.unsecuredCopyToClipboard(this.data)
            }
            this.isCopied = true
            setTimeout(() => this.isCopied = false, 2000)
        },
    },
    mounted() {
        this.emitter.on("showModal", data => {
            this.data = `${window.location.host}/link/${data.link}` 
            this.openModal()
        })
    }
}
</script>
