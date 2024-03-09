<template>
<main class="mx-auto container font-base text-white">
    <div class="border-b border-dashed border-white/20  h-14 mt-5">
        <nav class="mx-5 lg:mx-0 bg-[#222326t] items-center flex justify-between">
            <a href="/" class="text-3xl text-[#d8fb4e] inline-flex gap-2 items-center">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-8 h-8">
                    <path fill-rule="evenodd" d="M2.25 6a3 3 0 0 1 3-3h13.5a3 3 0 0 1 3 3v12a3 3 0 0 1-3 3H5.25a3 3 0 0 1-3-3V6Zm3.97.97a.75.75 0 0 1 1.06 0l2.25 2.25a.75.75 0 0 1 0 1.06l-2.25 2.25a.75.75 0 0 1-1.06-1.06l1.72-1.72-1.72-1.72a.75.75 0 0 1 0-1.06Zm4.28 4.28a.75.75 0 0 0 0 1.5h3a.75.75 0 0 0 0-1.5h-3Z" clip-rule="evenodd" />
                </svg>
                codeit</a>
            <div class="hidden lg:flex gap-5 text-sm">
                <a target="_blank" href="https://www.buymeacoffee.com/nicklangat">Support Developers</a>
                <LinkModal />
            </div>
            <h1 class="text-3xl text-[#d8fb4e] inline-flex gap-2 items-center">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-8 h-8">
                    <path fill-rule="evenodd" d="M2.25 6a3 3 0 0 1 3-3h13.5a3 3 0 0 1 3 3v12a3 3 0 0 1-3 3H5.25a3 3 0 0 1-3-3V6Zm3.97.97a.75.75 0 0 1 1.06 0l2.25 2.25a.75.75 0 0 1 0 1.06l-2.25 2.25a.75.75 0 0 1-1.06-1.06l1.72-1.72-1.72-1.72a.75.75 0 0 1 0-1.06Zm4.28 4.28a.75.75 0 0 0 0 1.5h3a.75.75 0 0 0 0-1.5h-3Z" clip-rule="evenodd" />
                </svg>
            </h1>
        </nav>
    </div>
    <div class="grid lg:mt-5 lg:grid-cols-2 gap-10 mx-5 lg:mx-0">
        <div class="mt-10 w-full">
            <div class="flex mt-2 w-full gap-4 flex-col">
                <label for="" class="text-2xl">Paste your code below</label>
                <textarea class="shadow-lg border bg-inherit text-stone-400 border-neutral-600 w-full pl-4 rounded-xl  focus:ring-0 focus:outline-none" rows="24" v-model="code"></textarea>
            </div>
        </div>
        <div class="lg:mt-10 w-full">

            <div class="flex w-full justify-between items-center">

                <div class="flex gap-2 items-center">
                    <span :class="currentBackground == cssClasses[0] ? 'ring ring-white': ''" @click="setBackground(0)" class="bg-gradient-to-r ring-white from-[#3bbaf8] via-[#5396f5] to-[#606ff2] hover:ring h-6 cursor-pointer rounded-full w-6"></span>
                    <span :class="currentBackground == cssClasses[1] ? 'ring ring-white': ''" @click="setBackground(1)" class="bg-gradient-to-r from-[#340462] via-[#8b04c3] to-[#f101a5] h-6 cursor-pointer hover:ring transition-all duration-300 ring-white rounded-full w-6"></span>
                    <span :class="currentBackground == cssClasses[2] ? 'ring ring-white': ''" @click="setBackground(2)" class="bg-gradient-to-r from-[#93f9b9] via-[#93f9b9] to-[#1d976c] h-6 cursor-pointer hover:ring transition-all duration-300 ring-white rounded-full w-6"></span>

                </div>
                <div v-if="code" class="flex gap-5">
                    <button @click="saveCode" class="bg-[#167dff] inline-flex gap-2 items-center py-1.5 px-4 text-sm rounded-md">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M13.19 8.688a4.5 4.5 0 0 1 1.242 7.244l-4.5 4.5a4.5 4.5 0 0 1-6.364-6.364l1.757-1.757m13.35-.622 1.757-1.757a4.5 4.5 0 0 0-6.364-6.364l-4.5 4.5a4.5 4.5 0 0 0 1.242 7.244" />
                        </svg>

                        Share code</button>
                    <button v-if="!isCopied" @click="copyCode" class="bg-[#d8fb4e] text-black/70 inline-flex gap-2 items-center py-1.5 px-4 text-sm rounded-md">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 0 0 2.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 0 0-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75 2.25 2.25 0 0 0-.1-.664m-5.8 0A2.251 2.251 0 0 1 13.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V9.375c0-.621-.504-1.125-1.125-1.125H8.25ZM6.75 12h.008v.008H6.75V12Zm0 3h.008v.008H6.75V15Zm0 3h.008v.008H6.75V18Z" />
                        </svg>
                        Copy code</button>
                    <button v-if="isCopied" class="bg-[#d8fb4e] text-black/70 inline-flex gap-2 items-center py-1.5 px-4 text-sm rounded-md">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4 text-primary">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                        </svg>
                        Code copied</button>
                </div>
            </div>
            <div :class="currentBackground" class=" pb-3 rounded-xl mt-5 bg-gradient-to-r">
                <highlightjs class="p-3" theme="tokyo-night-dark.min" language="autodetect" :code=code />
            </div>

        </div>

    </div>
    <!-- </div> -->

</main>
</template>

<script>
import axios from 'axios';
import 'highlight.js/lib/common';
import hljsVuePlugin from "@highlightjs/vue-plugin";
import 'highlight.js/styles/tokyo-night-dark.min.css';
import 'highlight.js/styles/felipec.min.css';
import LinkModal from '@/components/LinkModal.vue';
// import 'highlight.js/styles/qtcreator-dark.min.css';
export default {
    components: {
        highlightjs: hljsVuePlugin.component,
        LinkModal
    },
    data() {
        return {
            code: "",
            baseURL: process.env.VUE_APP_BASE_URL,
            isCopied: false,
            cssClasses: [
                "from-[#3bbaf8] via-[#5396f5] to-[#606ff2]",
                "from-[#340462] via-[#8b04c3] to-[#f101a5]",
                "from-[#93f9b9] via-[#93f9b9] to-[#1d976c]"
            ],
            currentBackground: "from-[#3bbaf8] via-[#5396f5] to-[#606ff2]",
        }
    },
    methods: {
        setBackground(index) {
            this.currentBackground = this.cssClasses[index]
        },
        saveCode() {
            if (this.code.length) {
                axios.post(`${this.baseURL}codes/`, {
                    "snippet": this.code
                }).then((res) => {

                    this.generateLink(res.data.id)
                })
            }
        },
        generateLink(code) {
            axios.post(`${this.baseURL}links/`, {
                "code": code
            }).then(res => {
                // open modal with shared link ready
                this.emitter.emit("showModal", {
                    "link": res.data.link
                })
            })
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
        copyCode() {
            if (window.isSecureContext && navigator.clipboard) {
                navigator.clipboard.writeText(this.code)
            } else {
                this.unsecuredCopyToClipboard(this.code)
            }
            this.isCopied = true
            setTimeout(() => this.isCopied = false, 2000)
        },
    }
}
</script>

<style>
code {
    border-radius: 12px;
    height: 34rem;
    width: 100%;
}

body,
html {
    background-color: #151515;
    /* #111216; */
}
</style>
